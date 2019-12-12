object Digits {


  /**
    * Project Euler problem 63
    * @return
    */

  def countNDigitNumbersWhichAreAlsoNthPowers(): Int = {
    var count = 0
    var m = 1

    for (n <- 1 to 9) {
      var d = countDigitsInPower(n, m)
      while (d >= m) {
        if (d == m) {
          println(s"$n to the power of $m is of $d digits")
          count += 1
        }
        m += 1
        d = countDigitsInPower(n, m)
      }
      m = 1
    }
    count
  }

  def countDigitsInPower(x: Int, y: Int): Int = {
    (1 + y * Math.log10(x)).toInt
  }

}

