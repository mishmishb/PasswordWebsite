// Transcrypt'ed from Python, 2019-06-09 23:38:42
var itertools = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {FREQUENCY_LISTS, L33T_CHARACTERS} from './data.js';
import * as __module_itertools__ from './itertools.js';
__nest__ (itertools, '', __module_itertools__);
var __name__ = '__main__';
export var RANKED_WORDLISTS = dict ({});
export var dictionary_ranker = function () {
	for (var [py_name, dictionary_words] of FREQUENCY_LISTS.py_items ()) {
		RANKED_WORDLISTS [py_name] = (function () {
			var __accu0__ = [];
			for (var [rank, word] of enumerate (dictionary_words, 1)) {
				__accu0__.append ([word, rank]);
			}
			return dict (__accu0__);
		}) ();
	}
	return RANKED_WORDLISTS;
};
export var word_finder = function (password, ranked_wordlists) {
	var found_words = [];
	for (var finder of [dictionary_finder, l33t_finder]) {
		found_words.extend (finder (password, ranked_wordlists));
	}
	return sorted (found_words, __kwargtrans__ ({key: (function __lambda__ (x) {
		return tuple ([x ['length'], !(x ['l33t']), -(x ['rank'])]);
	}), reverse: true}));
};
export var dictionary_finder = function (password, ranked_wordlists) {
	var found_words = [];
	var length = len (password);
	var password_lower = password.lower ();
	for (var [py_name, word_list] of ranked_wordlists.py_items ()) {
		for (var start = 0; start < length; start++) {
			for (var end = start; end < length; end++) {
				if (__in__ (password_lower.__getslice__ (start, end + 1, 1), word_list)) {
					var word = password_lower.__getslice__ (start, end + 1, 1);
					var rank = word_list [word];
					found_words.append (dict ({'start': start, 'end': end, 'pattern_type': 'dictionary', 'input': password.__getslice__ (start, end + 1, 1), 'length': len (word), 'word_list': py_name, 'found_word': word, 'rank': rank, 'l33t': false}));
				}
			}
		}
	}
	return found_words;
};
export var generate_l33t_dict = function (password, l33t_dict) {
	var nonalpha = (function () {
		var __accu0__ = [];
		for (var a of password) {
			if (!(a.isalpha ())) {
				__accu0__.append (a);
			}
		}
		return __accu0__;
	}) ();
	var swaps = dict ({});
	for (var n_a of nonalpha) {
		var swapped_letters = (function () {
			var __accu0__ = [];
			for (var [lettrs, l33ts] of l33t_dict.py_items ()) {
				if (__in__ (n_a, l33ts)) {
					__accu0__.append (lettrs);
				}
			}
			return __accu0__;
		}) ();
		if (swapped_letters) {
			swaps [n_a] = swapped_letters;
		}
	}
	return swaps;
};
export var l33t_finder = function (password, ranked_wordlists) {
	var found_words = [];
	var l33t_dict = generate_l33t_dict (password, L33T_CHARACTERS);
	var password_options = [];
	for (var value of password) {
		var is_l33t = false;
		for (var [l33t, letter] of l33t_dict.py_items ()) {
			if (l33t == value) {
				password_options.append (letter);
				var is_l33t = true;
				break;
			}
		}
		if (is_l33t === false) {
			password_options.append (value);
		}
	}
	var password_permutations = (function () {
		var __accu0__ = [];
		for (var perm of list (itertools.product (...password_options))) {
			__accu0__.append (''.join (perm));
		}
		return __accu0__;
	}) ();
	for (var permutation of password_permutations) {
		for (var word of dictionary_finder (permutation, ranked_wordlists)) {
			if (word ['length'] > 1) {
				var sequence = password.__getslice__ (word ['start'], word ['end'] + 1, 1);
				if (sequence.lower () == word ['found_word']) {
					continue;
				}
				var swap = dict ({});
				for (var [l33t, letter] of l33t_dict.py_items ()) {
					var swap_list = (function () {
						var __accu0__ = [];
						for (var [pos, char] of enumerate (sequence)) {
							if (l33t == char) {
								__accu0__.append (word ['found_word'] [pos]);
							}
						}
						return __accu0__;
					}) ();
					if (swap_list) {
						swap [l33t] = swap_list;
					}
				}
				word ['l33t'] = true;
				word ['input'] = sequence;
				word ['swap'] = swap;
				found_words.append (word);
			}
		}
	}
	return found_words;
};

//# sourceMappingURL=word_extraction.map