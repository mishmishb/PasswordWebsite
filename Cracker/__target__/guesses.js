// Transcrypt'ed from Python, 2019-05-31 23:15:38
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
var __name__ = 'guesses';
export var MALE_NAMES = 1219;
export var FEMALE_NAMES = 4275;
export var ENGLISH_WIKIPEDIA = 100000;
export var SURNAMES = 88799;
export var US_TV_AND_FILM = 39070;
export var PASSWORDS = 47023;
export var nCk = function (n, k) {
	if (k > n) {
		return 0;
	}
	if (k == 0) {
		return 1;
	}
	var r = 1;
	for (var d = 1; d < k + 1; d++) {
		r *= n;
		r /= d;
		n--;
	}
	return r;
};
export var guess_calculator = function (password) {
	var guesses = 0;
	for (var match of password) {
		if (match ['pattern'] == 'dictionary') {
			guesses += dictionary_guess (match, match ['dictionary_name']);
		}
		else {
			guesses += bruteforce_guesses (match);
		}
	}
	return guesses;
};
export var bruteforce_guesses = function (match) {
	var low_alpha = false;
	var upper_alpha = false;
	var number = false;
	var symbol = false;
	var potential_symbols = '!"£$€%^&*()-_=+[]{}#~\'@/?.>,<|\\`¬';
	var search_space = 0;
	var sequence = match ['token'];
	for (var chr of sequence) {
		if (chr.islower () && low_alpha == false) {
			search_space += 26;
			var low_alpha = true;
		}
		else if (chr.isupper () && upper_alpha == false) {
			search_space += 26;
			var upper_alpha = true;
		}
		else if (chr.isdecimal () && number == false) {
			search_space += 10;
			var number = true;
		}
		else if (__in__ (chr, potential_symbols) && symbol == false) {
			search_space += 33;
			var symbol = true;
		}
	}
	var entropy = math.log2 (Math.pow (search_space, len (sequence)));
	var brute_guess = round (Math.pow (2, entropy) / 2);
	return brute_guess;
};
export var dictionary_guess = function (match, dictionary_name) {
	if (dictionary_name == 'passwords') {
		var dictionary_length = PASSWORDS;
	}
	else if (dictionary_name == 'english_wikipedia') {
		var dictionary_length = ENGLISH_WIKIPEDIA;
	}
	else if (dictionary_name == 'us_tv_and_film') {
		var dictionary_length = US_TV_AND_FILM;
	}
	else if (dictionary_name == 'male_names') {
		var dictionary_length = MALE_NAMES;
	}
	else if (dictionary_name == 'female_names') {
		var dictionary_length = FEMALE_NAMES;
	}
	else if (dictionary_name == 'surnames') {
		var dictionary_length = SURNAMES;
	}
	var upper_loops = uppercase_character_loops (match);
	var l33t_loops = l33t_character_loops (match);
	var guesses = (match ['rank'] + dictionary_length * upper_loops) + dictionary_length * l33t_loops;
	return guesses;
};
export var uppercase_character_loops = function (match) {
	var word = match ['token'];
	if (word.islower ()) {
		return 0;
	}
	var alpha_only = (function () {
		var __accu0__ = [];
		for (var chr of word) {
			if (chr.isalpha ()) {
				__accu0__.append (chr);
			}
		}
		return __accu0__;
	}) ();
	var uppercase_count = 0;
	var lowercase_count = 0;
	for (var letter of alpha_only) {
		if (letter.isupper ()) {
			uppercase_count++;
		}
	}
	if (word [0].isupper () && uppercase_count == 1) {
		return 1;
	}
	if (word [len(word) - 1].isupper () && uppercase_count == 1 || word.isupper ()) {
		return 2.5;
	}
	var dictionary_loops = 0;
	for (var k = 1; k < uppercase_count + 1; k++) {
		if (k == uppercase_count) {
			dictionary_loops += nCk (len (alpha_only), k) / 2;
		}
		else {
			dictionary_loops += nCk (len (alpha_only), k);
		}
	}
	return dictionary_loops;
};
export var l33t_character_loops = function (match) {
	if (!(match.py_get ('l33t', false))) {
		return 0;
	}
	var variations = 1;
	for (var [subbed, unsubbed] of match ['sub'].py_items ()) {
		var chrs = list (match ['token'].lower ());
		var S = sum ((function () {
			var __accu0__ = [];
			for (var chr of chrs) {
				if (chr == subbed) {
					__accu0__.append (1);
				}
			}
			return py_iter (__accu0__);
		}) ());
		var U = sum ((function () {
			var __accu0__ = [];
			for (var chr of chrs) {
				if (chr == unsubbed) {
					__accu0__.append (1);
				}
			}
			return py_iter (__accu0__);
		}) ());
		if (S == 0 || U == 0) {
			variations *= 2;
		}
		else {
			var p = min (U, S);
			var possibilities = 0;
			for (var i = 1; i < p + 1; i++) {
				possibilities += nCk (U + S, i);
			}
			variations *= possibilities;
		}
	}
	return variations;
};

//# sourceMappingURL=guesses.map