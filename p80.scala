package in.umlaut.euler

object DigitalSumOfSquareRoots {
  /**
    * Solves project euler problem 80
    * @return
    */
  def getSumOfFirstHundredDigits:Int = (1 to 100) map (x => getSquareRootDecimals(x)._2) sum
  
  /**
    * Retuns the square of an integer
    * returns only the integer value and not any decimal portion
    * i.e., for input 26, output would be 5
    * @param n
    * @return
    */

  def getSquareRootWholeInteger(n: Int): (Int, Int) = {
    def iterateUp(i: Int, n: Int): (Int, Int) = {
      if (i * i < n) {
        iterateUp(i + 1, n)
      }
      else if (i * i == n) {
        (i, 0)
      }
      else {
        (i - 1, n - (i-1)*(i-1))
      }
    }
    require(n >= 0, "the number must be non-negative.")
    iterateUp(1, n)
  }

  /**
    * Returns square root of an integer up to 100 digits (99 after decimal points)
    * and the sum of all digits
    * Uses the old-school method of division and digit-by-digit calculation
    * @param n
    * @return
    */
  def getSquareRootDecimals(n: Int): (BigInt, Int) = {
    require(n >= 0, "the number must be non-negative.")

    def getSquareRootDecimalsHelper(dividend: BigInt, p: BigInt, count: Int, sum:Int):(BigInt, Int) = {
      if (count == 99) {
        (p, sum)
      } else {
        val np = getNextPartialResult(dividend, p, 1)
        getSquareRootDecimalsHelper(np._2 * 100, np._1 + 10*p, count + 1, sum + np._1)
      }
    }

    def getNextPartialResult(dividend: BigInt, p:BigInt, x: Int): (Int, BigInt) = {
      if ((20 * p + x) * x < dividend) {
        getNextPartialResult(dividend, p, x + 1)
      }
      else {
        (x - 1, dividend - ((20 * p + (x - 1)) * (x - 1)))
      }
    }

    val p = getSquareRootWholeInteger(n)
    val r = p._2
    if (r == 0){
      (BigInt.apply(0),0)
    } else {
      getSquareRootDecimalsHelper(BigInt.apply(r * 100), p._1, 0, p._1)
    }
  }

}
