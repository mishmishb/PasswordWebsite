// Transcrypt'ed from Python, 2019-06-09 15:33:40
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'find_sequence';
export var make_sequence = function (password, found_words) {
	var output = [];
	var used_entries = [];
	var brute = [];
	var brute_positions = [];
	var password_buffer = list (password);
	for (var word of found_words) {
		if (!__in__ (word ['start'], used_entries)) {
			if (!__in__ (word ['end'], used_entries)) {
				output.append (word);
				for (var character = word ['start']; character < word ['end'] + 1; character++) {
					password_buffer [character] = 'OUT';
					used_entries.append (character);
				}
			}
		}
	}
	var position_help = len (password_buffer) - 1;
	for (var [position, value] of enumerate (password_buffer)) {
		if (value != 'OUT') {
			brute.extend ([value]);
			brute_positions.append (position);
		}
		if (value == 'OUT' && len(brute) > 0 || position == position_help && len(brute) > 0) {
			var bf_word = ''.join (brute);
			output.append (dict ({'start': brute_positions [0], 'end': brute_positions [len(brute_positions) - 1], 'pattern_type': 'bruteforce', 'input': bf_word, 'length': len (bf_word)}));
			var brute = [];
			var brute_positions = [];
		}
	}
	return sorted (output, __kwargtrans__ ({key: (function __lambda__ (x) {
		return x ['start'];
	})}));
};

//# sourceMappingURL=find_sequence.map