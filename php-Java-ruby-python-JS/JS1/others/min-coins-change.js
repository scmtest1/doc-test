(function (exports) {
  'use strict';

  /**
   * Returns the minimum number of coins from given set,
   * which sum equals to given change. This is famous
   * problem from the dymanic programming:
   *   https://en.wikipedia.org/wiki/Change-making_problem
   *
   * @public
   * @module others/minCoinsChange
   *
   * @example
   *
   * var minCoinsChange =
   *  require('path-to-algorithms/src/others/min-coins-change')
   *  .minCoinsChange;
   * var coins = minCoinsChange([1, 2, 3], 5); // [ 2, 3 ]
   *
   * @param {Array} coins The sorted list of the coins used for the change.
   * @param {Number} change The change, which should be returned.
   * @return Array which contains the minimum coins from the given
   *  list, required for the change.
   */
  function minCoinsChange(coins, change) {
    var minChange = [[0]];
    if (coins.indexOf(change) >= 0) {
      return [change];
    }
    for (var i = 1; i <= change; i += 1) {
      var current = null;
      for (var j = 0; j < coins.length && coins[j] <= change; j += 1) {
        for (var k = 0; k < minChange.length; k += 1) {
          if (k + coins[j] === i &&
             (!current || minChange[k].length + 1 < current.length)) {
            minChange[i] = minChange[k].concat([coins[j]]);
          }
        }
      }
    }
    var result = minChange[change];
    if (!result) {
      return undefined;
    }
    return result.slice(1);
  }

  exports.minCoinsChange = minCoinsChange;
 
  function unintendedGlobal() {
    var x = y = "something"; //Defect
  }
 
  function stray_semicolon_to_fix(x) {
    for (var i = 0; i < x; i++); { // STRAY_SEMICOLON here
    something(i);
    }
  }

})(typeof window === 'undefined' ? module.exports : window);
