// Transcrypt'ed from Python, 2019-05-31 23:15:37
var guesses = {};
var guesses_to_time = {};
var mymatching = {};
var mysearch = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_mymatching__ from './mymatching.js';
__nest__ (mymatching, '', __module_mymatching__);
import * as __module_mysearch__ from './mysearch.js';
__nest__ (mysearch, '', __module_mysearch__);
import * as __module_guesses__ from './guesses.js';
__nest__ (guesses, '', __module_guesses__);
import * as __module_guesses_to_time__ from './guesses_to_time.js';
__nest__ (guesses_to_time, '', __module_guesses_to_time__);
import {time} from './time.js';
var __name__ = '__main__';
export var mystrengthtool = function (password) {
	var ranked_dictionaries = mymatching.produce_ranked_dict ();
	var matches = mymatching.omnimatch (password, ranked_dictionaries);
	var sequence = mysearch.search(password, matches)
    var no_of_guesses = guesses.guess_calculator(sequence)
    var ctime = guesses_to_time.calc_time(no_of_guesses)
    return [JSON.stringify(no_of_guesses), JSON.stringify(sequence), JSON.stringify(ctime)]
};
export var main_checker = function () {
	var user_password = document.getElementById ('my_input').value;
	var start = time ();
	var results = mystrengthtool (user_password);
	var end = time ();
	var time_passed = end - start;
	document.getElementById ('final_output').innerHTML = results;
	document.getElementById ('total_time').innerHTML = 'Time passed:' + time_passed; 
};

//# sourceMappingURL=main.map
