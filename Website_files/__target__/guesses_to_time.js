// Transcrypt'ed from Python, 2019-06-09 15:33:40
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'guesses_to_time';
export var display_time = function (seconds) {
	var minutes = seconds / 60;
	var hours = minutes / 60;
	var days = hours / 24;
	var months = days / 31;
	var years = months / 12;
	if (seconds < 60) {
		var readable_time = '{} second'.format (round (seconds));
	}
	else if (minutes < 60) {
		var readable_time = '{} minute'.format (round (minutes));
	}
	else if (hours < 24) {
		var readable_time = '{} hour'.format (round (hours));
	}
	else if (days < 31) {
		var readable_time = '{} day'.format (round (days));
	}
	else if (months < 12) {
		var readable_time = '{} month'.format (round (months));
	}
	else {
		var readable_time = '{} year'.format (round (years));
	}
	if (readable_time.py_split (' ') [0] != '1') {
		readable_time += 's';
	}
	return readable_time;
};
export var calculate_crack_time = function (guesses) {
	var online_throttled = display_time (guesses / (1 / 36));
	var online_unthrottled = display_time (guesses / 10.0);
	var offline_slow_hash = display_time (guesses / 10000.0);
	var offline_fast_hash = display_time (guesses / 10000000000.0);
	var times_to_crack = dict ({'Throttled online attack:\t': online_throttled, 'Unthrottled online attack:\t': online_unthrottled, 'Slow hash offline attack:\t': offline_slow_hash, 'Fast hash  offline attack:\t': offline_fast_hash});
	return times_to_crack;
};

//# sourceMappingURL=guesses_to_time.map