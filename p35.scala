package in.umlaut.euler

object CircularPrimes {

  /**
    * Gets the circular prime numbers under the limit n
    * Project Euler 35
    * @param n
    * @return
    */
  def getCircularPrimes(n: Int):Int = {
    def isProbableCircularPrime(x: Int):Boolean = {
      if(x < 10) {
        true
      } else {
        (Set(1,3,7,9) contains(x % 10)) && isProbableCircularPrime(x / 10)
      }
    }
    val primes = getPrimesTillN(n).toSet
    val circularPrimes = primes.filter(p => isProbableCircularPrime(p)).filter(p => generateRotations(p).toSet.subsetOf(primes))
    circularPrimes.size
  }
  
def generateRotations(n:Int):List[Int] = (1 to n.toString.length) map(i => shiftRight(n, i)) toList

  /**
    * Sieve of Eratosthenes taken from https://gist.github.com/mattfowler/62f1be4fbe6d36c0a9d84c94817389ba
    * @param n
    * @return
    */
  def getPrimesTillN(n: Int):List[Int] = {
    val odds = Stream.from(3, 2).takeWhile(_ <= Math.sqrt(n).toInt)
    val composites = odds.flatMap(i => Stream.from(i * i, 2 * i).takeWhile(_ <= n))
    2 :: Stream.from(3, 2).takeWhile(_ <= n).diff(composites).toList
  }

}
