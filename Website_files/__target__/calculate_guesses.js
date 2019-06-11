// Transcrypt'ed from Python, 2019-06-09 23:38:06
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {FREQUENCY_LISTS, L33T_CHARACTERS} from './data.js';
var __name__ = '__main__';
export var combination_count = function (n, r) {
	var r = min (r, n - r);
	if (r == 0) {
		return 1;
	}
	var res = 1;
	for (var k = 1; k < r + 1; k++) {
		var res = (res * ((n - k) + 1)) / k;
	}
	return res;
};
export var guess_calculator = function (sequence) {
	var guesses = 1;
	for (var section of sequence) {
		if (section ['pattern_type'] == 'dictionary') {
			guesses *= dictionary_guesses (section, section ['word_list']);
		}
		else {
			guesses *= bruteforce_guesses (section);
		}
	}
	return guesses;
};
export var bruteforce_guesses = function (section) {
	var low_alpha = false;
	var upper_alpha = false;
	var number = false;
	var symbol = false;
	var potential_symbols = '!"£$€%^&*()-_=;:+[]{}#~\\\'@/?.>,<|`¬';
	var set_size = 0;
	var input_string = section ['input'];
	for (var character of input_string) {
		if (character.islower () && low_alpha === false) {
			set_size += 26;
			var low_alpha = true;
		}
		else if (character.isupper () && upper_alpha === false) {
			set_size += 26;
			var upper_alpha = true;
		}
		else if (character.isdecimal () && number === false) {
			set_size += 10;
			var number = true;
		}
		else if (__in__ (character, potential_symbols) && symbol === false) {
			set_size += 35;
			var symbol = true;
		}
	}
	var brute_guess = round (Math.pow (set_size, len (input_string)) / 2);
	var space = [];
	if (low_alpha === true) {
		space.append ('lowercase');
	}
	if (upper_alpha === true) {
		space.append ('uppercase');
	}
	if (number === true) {
		space.append ('number');
	}
	if (symbol === true) {
		space.append ('symbol');
	}
	section ['character_space'] = space;
	return brute_guess;
};
export var dictionary_guesses = function (section, dictionary_name) {
	var dictionary_length = len (FREQUENCY_LISTS [dictionary_name]);
	var upper_loops = uppercase_character_loops (section);
	var l33t_loops = l33t_character_loops (section);
	var guesses = (section ['rank'] + dictionary_length * upper_loops) + dictionary_length * l33t_loops;
	section ['guesses'] = guesses;
	return guesses;
};
export var uppercase_character_loops = function (section) {
	var word = section ['input'];
	if (word.islower ()) {
		return 0;
	}
	var alpha_only = (function () {
		var __accu0__ = [];
		for (var a of word) {
			if (a.isalpha ()) {
				__accu0__.append (a);
			}
		}
		return __accu0__;
	}) ();
	var uppercase_count = 0;
	for (var letter of alpha_only) {
		if (letter.isupper ()) {
			uppercase_count++;
		}
	}
	if (word [0].isupper () && uppercase_count == 1 || word.isupper ()) {
		section ['uppercase_style'] = 'First or ALL';
		return 1;
	}
	var dictionary_loops = 0;
	for (var k = 1; k < uppercase_count + 1; k++) {
		if (k == uppercase_count) {
			dictionary_loops += combination_count (len (alpha_only), k) / 2;
		}
		else {
			dictionary_loops += combination_count (len (alpha_only), k);
		}
	}
	section ['upppercase_style'] = 'Good';
	return dictionary_loops;
};
export var l33t_character_loops = function (section) {
	var token_lower = section ['input'].lower ();
	if (token_lower == section ['found_word']) {
		return 0;
	}
	var alpha_only = (function () {
		var __accu0__ = [];
		for (var a of token_lower) {
			if (a.isalpha ()) {
				__accu0__.append (a);
			}
		}
		return __accu0__;
	}) ();
	var potential_swaps = len ((function () {
		var __accu0__ = [];
		for (var l of alpha_only) {
			if (__in__ (l, L33T_CHARACTERS.py_keys ())) {
				__accu0__.append (l);
			}
		}
		return __accu0__;
	}) ()) + len (section ['swap']);
	var dictionary_loops = 0;
	for (var k = 1; k < len (section ['swap']) + 1; k++) {
		if (k == potential_swaps) {
			dictionary_loops += combination_count (potential_swaps, k) / 2;
		}
		else {
			dictionary_loops += combination_count (potential_swaps, k);
		}
	}
	return dictionary_loops;
};

//# sourceMappingURL=calculate_guesses.map