object Primes {

  /**
    * Project euler problem 58
    * @param limit
    * @return
    */

  def spiralPrimes(limit: Double): Int = {

    def getTotalDiagonalElements(n: Int): Int = {
      1 + 4 * n
    }

    def getSideLength(n: Int): Int = {
      2 * n + 1
    }

    def getPercentageOfPrimes(p: Int, n: Int): Double = {
      (p * 100f) / getTotalDiagonalElements(n)
    }

    def getNextDiagCorners(n: Int): List[Int] = {
      val a = 4 * n * n
      val b = 2 * n
      List(
        a - b + 1,
        a + 1,
        a + b + 1
      )
    }

    var primeCount = 0
    var n = 0
    var percentOfPrimes = 100d

    while (percentOfPrimes >= limit) {
      n = n + 1
      primeCount = primeCount + getNextDiagCorners(n).count(isPrime)
      percentOfPrimes = getPercentageOfPrimes(primeCount, n)
    }

    getSideLength(n)
  }


/**
    * Checks if an integer is prime or not
    * @param n
    * @return
    */
  def isPrime(n:Int): Boolean = {
    if (n <= 1) {
      false
    }

    else if (n <= 3) {
      true
    }

    else if (n % 2 == 0 || n % 3 == 0) {
      false
    }

    else {
      val sqrt = Math.sqrt(n).toInt
      val res = (for (i <- 5 to sqrt by 6
                    if (n % i == 0 || n % (i + 2) == 0) ) yield false).headOption

      res.isEmpty
    }
  }

}

