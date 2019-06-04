// Transcrypt'ed from Python, 2019-05-31 23:15:38
var itertools = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_itertools__ from './itertools.js';
__nest__ (itertools, '', __module_itertools__);
import {time} from './time.js';
import {FREQUENCY_LISTS} from './frequency_lists.js';
var __name__ = 'mymatching';
export var RANKED_DICTIONARIES = dict ({});
export var produce_ranked_dict = function () {
	var build_ranked_dict = function (ordered_list) {
		return (function () {
			var __accu0__ = [];
			for (var [idx, word] of enumerate (ordered_list, 1)) {
				__accu0__.append ([word, idx]);
			}
			return dict (__accu0__);
		}) ();
	};
	var add_frequency_lists = function (frequency_lists_) {
		for (var [py_name, lst] of frequency_lists_.py_items ()) {
			RANKED_DICTIONARIES [py_name] = build_ranked_dict (lst);
		}
	};
	add_frequency_lists (FREQUENCY_LISTS);
	return RANKED_DICTIONARIES;
};
export var L33T_TABLE = dict ({'a': ['4', '@'], 'b': ['8'], 'c': ['(', '{', '[', '<'], 'e': ['3'], 'g': ['6', '9'], 'i': ['1', '!', '|'], 'l': ['1', '|', '7'], 'o': ['0'], 's': ['$', '5'], 't': ['+', '7'], 'x': ['%'], 'z': ['2']});
export var omnimatch = function (password, _ranked_dictionaries) {
	if (typeof _ranked_dictionaries == 'undefined' || (_ranked_dictionaries != null && _ranked_dictionaries.hasOwnProperty ("__kwargtrans__"))) {;
		var _ranked_dictionaries = RANKED_DICTIONARIES;
	};
	var matches = [];
	for (var matcher of [dictionary_match, my_l33t_match]) {
		matches.extend (matcher (password, __kwargtrans__ ({_ranked_dictionaries: _ranked_dictionaries})));
	}
	return sorted (matches, __kwargtrans__ ({key: (function __lambda__ (x) {
		return x ['matched_length'];
	}), reverse: true}));
};
export var dictionary_match = function (password, _ranked_dictionaries) {
	if (typeof _ranked_dictionaries == 'undefined' || (_ranked_dictionaries != null && _ranked_dictionaries.hasOwnProperty ("__kwargtrans__"))) {;
		var _ranked_dictionaries = RANKED_DICTIONARIES;
	};
	var matches = [];
	var length = len (password);
	var password_lower = password.lower ();
	for (var [dictionary_name, ranked_dict] of _ranked_dictionaries.py_items ()) {
		for (var i = 0; i < length; i++) {
			for (var j = i; j < length; j++) {
				if (__in__ (password_lower.__getslice__ (i, j + 1, 1), ranked_dict)) {
					var word = password_lower.__getslice__ (i, j + 1, 1);
					var rank = ranked_dict [word];
					matches.append (dict ({'pattern': 'dictionary', 'i': i, 'j': j, 'token': password.__getslice__ (i, j + 1, 1), 'matched_word': word, 'matched_length': len (word), 'rank': rank, 'dictionary_name': dictionary_name, 'l33t': false}));
				}
			}
		}
	}
	return sorted (matches, __kwargtrans__ ({key: (function __lambda__ (x) {
		return tuple ([x ['i'], x ['j']]);
	})}));
};
export var alternative_l33t_table = function (password, table) {
	var password_chars = set (password);
	var nonalpha = (function () {
		var __accu0__ = [];
		for (var a of password_chars) {
			if (!(a.isalpha ())) {
				__accu0__.append (a);
			}
		}
		return __accu0__;
	}) ();
	var matches = dict ({});
	for (var chr of nonalpha) {
		var temp = (function () {
			var __accu0__ = [];
			for (var [k, v] of table.py_items ()) {
				if (__in__ (chr, v)) {
					__accu0__.append (k);
				}
			}
			return __accu0__;
		}) ();
		if (temp) {
			matches [chr] = temp;
		}
	}
	return matches;
};
export var my_l33t_match = function (password, _ranked_dictionaries, _l33t_table) {
	if (typeof _ranked_dictionaries == 'undefined' || (_ranked_dictionaries != null && _ranked_dictionaries.hasOwnProperty ("__kwargtrans__"))) {;
		var _ranked_dictionaries = RANKED_DICTIONARIES;
	};
	if (typeof _l33t_table == 'undefined' || (_l33t_table != null && _l33t_table.hasOwnProperty ("__kwargtrans__"))) {;
		var _l33t_table = L33T_TABLE;
	};
	var matches = [];
	var my_l33t_table = alternative_l33t_table (password, _l33t_table);
	var password_list = list (password);
	var password_options = [];
	for (var i of password_list) {
		var is_l33t = false;
		for (var [k, v] of my_l33t_table.py_items ()) {
			if (k == i) {
				password_options.append (v);
				var is_l33t = true;
				break;
			}
		}
		if (is_l33t == false) {
			password_options.append (i);
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
		for (var match of dictionary_match (permutation, _ranked_dictionaries)) {
			var token = password.__getslice__ (match ['i'], match ['j'] + 1, 1);
			if (token.lower () == match ['matched_word']) {
				continue;
			}
			var match_sub = dict ({});
			for (var [chr, letter] of my_l33t_table.py_items ()) {
				if (__in__ (chr, token)) {
					for (var lttr of letter) {
						if (__in__ (lttr, match ['matched_word'])) {
							match_sub [chr] = lttr;
						}
					}
				}
			}
			match ['l33t'] = true;
			match ['token'] = token;
			match ['sub'] = match_sub;
			match ['sub_display'] = ', '.join ((function () {
				var __accu0__ = [];
				for (var [k, v] of match_sub.py_items ()) {
					__accu0__.append (__mod__ ('%s -> %s', tuple ([k, v])));
				}
				return __accu0__;
			}) ());
			matches.append (match);
		}
	}
	var matches = (function () {
		var __accu0__ = [];
		for (var match of matches) {
			if (len (match ['token']) > 1) {
				__accu0__.append (match);
			}
		}
		return __accu0__;
	}) ();
	return sorted (matches, __kwargtrans__ ({key: (function __lambda__ (x) {
		return tuple ([x ['i'], x ['j']]);
	})}));
};

//# sourceMappingURL=mymatching.map