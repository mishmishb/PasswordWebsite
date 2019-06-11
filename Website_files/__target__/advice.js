// Transcrypt'ed from Python, 2019-06-09 15:33:40
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'advice';
export var advice_generator = function (password, sequence) {
	var advice_dict = dict ({});
	general_advice (password, sequence, advice_dict);
	set_size_advice (password, advice_dict);
	bruteforce_advice (sequence, advice_dict);
	dictionary_advice (sequence, advice_dict);
	return advice_dict;
};
export var general_advice = function (password, sequence, advice_dict) {
	var advice_list = [];
	var length = len (password);
	if (length < 7) {
		advice_list.append ('This password is definitely too short!');
	}
	else if (length < 11) {
		advice_list.append ('Most passwords are around this length but you can definitely do better!');
	}
	else {
		advice_list.append ('This password is a good length');
	}
	for (var section of sequence) {
		if (section.py_get ('word_list')) {
			advice_list.append (' This password contains dictionary words and these are rarely that secure, have you tried using a mnemonic device?');
			break;
		}
	}

	advice_dict ['General: '] = advice_list;

	return advice_dict;
};
export var set_size_advice = function (password, advice_dict) {
	var advice_list = [];
	var set_list = [];
	var low_alpha = false;
	var upper_alpha = false;
	var number = false;
	var symbol = false;
	var potential_symbols = '!"£$€%^&*()-_=;:+[]{}#~\\\'@/?.>,<|`¬';
	for (var character of password) {
		if (character.islower () && low_alpha === false) {
			var low_alpha = true;
		}
		else if (character.isupper () && upper_alpha === false) {
			var upper_alpha = true;
		}
		else if (character.isdecimal () && number === false) {
			var number = true;
		}
		else if (__in__ (character, potential_symbols) && symbol === false) {
			var symbol = true;
		}
		if (!__in__ (false, tuple ([low_alpha, upper_alpha, number, symbol]))) {
			break;
		}
	}
	if (__in__ (false, tuple ([low_alpha, upper_alpha, number, symbol]))) {
		set_list.append ("This password doesn't contain");
		if (low_alpha === false) {
			set_list.append (' lowercase letters,');
		}
		if (upper_alpha === false) {
			set_list.append (' capital letters,');
		}
		if (number === false) {
			set_list.append (' numbers,');
		}
		if (symbol === false) {
			set_list.append (' symbols.');
		}
		advice_list.append (''.join (set_list).__getslice__ (0, -(1), 1) + '.');
	}
	else {
		advice_list.append ('This password contains a full set of characters, great!');
	}
	advice_dict ['Set size: '] = advice_list;
	return advice_dict;
};
export var bruteforce_advice = function (sequence, advice_dict) {
	var low_alpha = false;
	var upper_alpha = false;
	var number = false;
	var symbol = false;
	for (var section of sequence) {
		if (!(section.py_get ('word_list'))) {
			if (__in__ ('lowercase', section ['character_space'])) {
				var low_alpha = true;
			}
			if (__in__ ('uppercase', section ['character_space'])) {
				var upper_alpha = true;
			}
			if (__in__ ('number', section ['character_space'])) {
				var number = true;
			}
			if (__in__ ('symbol', section ['character_space'])) {
				var symbol = true;
			}
		}
	}
	if (__in__ (false, tuple ([low_alpha, upper_alpha, number, symbol]))) {
		advice_dict ['Brute-force: '] = ["The brute-force sections of the password don't contain a full character set, maybe expand this."];
	}
	if (!__in__ (true, tuple ([low_alpha, upper_alpha, number, symbol]))) {
		advice_dict ['Brute-force: '] = ['This password is entirely comprised of dictionary words'];
	}
	return advice_dict;
};
export var dictionary_advice = function (sequence, advice_dict) {
	for (var section of sequence) {
		var advice_list = [];
		if (section.py_get ('word_list')) {
			if (__in__ (section ['word_list'], tuple (['passwords', 'english_wikipedia', 'us_tv_and_film']))) {
				if (section ['rank'] <= 10) {
					advice_list.append ('{} is a top 10 most common word in {}'.format (section ['found_word'], section ['word_list']));
				}
				else if (section ['rank'] <= 100) {
					advice_list.append ('{} is a top 100 most common word in {}'.format (section ['found_word'], section ['word_list']));
				}
				else if (section ['rank'] <= 1000) {
					advice_list.append ('{} is a top 1000 most common word in {}'.format (section ['found_word'], section ['word_list']));
				}
				else if (section ['rank'] <= 10000) {
					advice_list.append ('{} is a top 10000 most common word in {}'.format (section ['found_word'], section ['word_list']));
				}
			}
			else if (__in__ (section ['word_list'], tuple (['male_names', 'female_names', 'surnames']))) {
				advice_list.append ('If this name is personally meaningful to you it is HIGHLY RECOMMENDED you avoid using it');
			}
			if (section.py_get ('uppercase_style')) {
				if (section ['uppercase_style'] == 'First or ALL') {
					advice_list.append (' This type of uppercasing is very obvious. Over 80% of uppercased words are either First letter uppercased or ALL uppercased.');
				}
			}
		}
		if (len(advice_list) > 0) {
			advice_dict [section ['input'] + ': '] = advice_list;
		}
	}
	return advice_dict;
};

//# sourceMappingURL=advice.map