// Transcrypt'ed from Python, 2019-06-01 01:11:36
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'guesses_to_time';
export var display_time = function (seconds) {
	var minute = 60;
	var hour = minute * 60;
	var day = hour * 24;
	var month = day * 31;
	var year = month * 12;
	var century = year * 100;
	if (seconds < 1) {
		var __left0__ = tuple ([seconds, '{} seconds'.format (seconds)]);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	if (seconds < minute) {
		var base = round (seconds);
		var __left0__ = tuple ([base, '{} second'.format (base)]);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	else if (seconds < hour) {
		var base = round (seconds / minute);
		var __left0__ = tuple ([base, '{} minute'.format (base)]);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	else if (seconds < day) {
		var base = round (seconds / hour);
		var __left0__ = tuple ([base, '{} hour'.format (base)]);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	else if (seconds < month) {
		var base = round (seconds / day);
		var __left0__ = tuple ([base, '{} day'.format (base)]);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	else if (seconds < year) {
		var base = round (seconds / month);
		var __left0__ = tuple ([base, '{} month'.format (base)]);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	else if (seconds < century) {
		var base = round (seconds / year);
		var __left0__ = tuple ([base, '{} year'.format (base)]);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	else {
		var __left0__ = tuple ([null, 'centuries']);
		var display_num = __left0__ [0];
		var display_str = __left0__ [1];
	}
	if (display_num && display_num != 1) {
		display_str += 's';
	}
	return display_str;
};
export var calc_time = function (guesses) {
	var online_throttled = display_time (guesses / (1 / 36));
	var online_unthrottled = display_time (guesses / 10.0);
	var offline_slow_hash = display_time (guesses / 10000.0);
	var offline_fast_hash = display_time (guesses / 10000000000.0);
	var times_to_crack = dict ({'Throttled online attack': online_throttled, 'Unthrottled online attack: ': online_unthrottled, 'Slow hash offline attack: ': offline_slow_hash, 'Fast hash  offline attack: ': offline_fast_hash});
	return times_to_crack;
};

//# sourceMappingURL=guesses_to_time.map