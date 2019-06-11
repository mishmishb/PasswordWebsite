// Transcrypt'ed from Python, 2019-06-09 15:33:40
var advice = {};
var calculate_guesses = {};
var find_sequence = {};
var guesses_to_time = {};
var word_extraction = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_advice__ from './advice.js';
__nest__ (advice, '', __module_advice__);
import * as __module_guesses_to_time__ from './guesses_to_time.js';
__nest__ (guesses_to_time, '', __module_guesses_to_time__);
import * as __module_calculate_guesses__ from './calculate_guesses.js';
__nest__ (calculate_guesses, '', __module_calculate_guesses__);
import * as __module_find_sequence__ from './find_sequence.js';
__nest__ (find_sequence, '', __module_find_sequence__);
import * as __module_word_extraction__ from './word_extraction.js';
__nest__ (word_extraction, '', __module_word_extraction__);
import {time} from './time.js';
var __name__ = '__main__';
export var mystrengthtool = function (input_password) {
	var ranked_wordlists = word_extraction.dictionary_ranker ();
	var extracted_words = word_extraction.word_finder (input_password, ranked_wordlists);
	var sequence = find_sequence.make_sequence (input_password, extracted_words);
	var no_of_guesses = calculate_guesses.guess_calculator (sequence);
	var password_advice = advice.advice_generator (input_password, sequence);
	var crack_time = guesses_to_time.calculate_crack_time (no_of_guesses);
	return [no_of_guesses, sequence, password_advice, crack_time];
};
export var main_checker = function() {
	var PASSWORD = document.getElementById ('my_input').value.py_replace (' ', '');
	var START = time ();
	var RESULTS = mystrengthtool (PASSWORD);
	var END = time ();
	var time_passed = END - START;
	document.getElementById ('number_of_guesses').innerHTML = 'No. of guesses: ' + JSON.stringify(RESULTS[0]);

	document.getElementById ('selected_sequence').innerHTML = 'Sequence: <ul>';
	for (var i of RESULTS [1]) {
		document.getElementById ('selected_sequence').innerHTML += '<li>' + JSON.stringify(i) +  '</li>';
	}
	document.getElementById ('selected_sequence').innerHTML += '</ul>';
	
	document.getElementById ('password_advice').innerHTML = 'Password advice: <ul>';
	for (var [k, v] of RESULTS[2].py_items()) {
		document.getElementById ('password_advice').innerHTML += '<li>' + k + JSON.parse(JSON.stringify(v)) + '</li>';
	}
	document.getElementById ('password_advice').innerHTML += '</ul>';
	
	document.getElementById ('crack_times').innerHTML = 'Crack times: <ul>';
	for (var[k, v] of RESULTS[3].py_items()) {
		document.getElementById ('crack_times').innerHTML += '<li>' + k + ': ' + v + '</li>';
	}
	document.getElementById ('crack_times').innerHTML += '</ul>';
	
	document.getElementById ('total_time').innerHTML = 'Time passed: ' + time_passed;
	
	if (!document.getElementById ('my_input').value)
	{
		document.getElementById ('number_of_guesses').innerHTML = [];
		document.getElementById ('selected_sequence').innerHTML = [];
		document.getElementById ('password_advice').innerHTML = [];
		document.getElementById ('crack_times').innerHTML = [];
		document.getElementById ('total_time').innerHTML = [];
	}
}

//# sourceMappingURL=main.map