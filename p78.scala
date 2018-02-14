package in.umlaut.euler

object CountPartitions {

  /**
    * Implements solution to Project Euler problem 78
    * @return
    */
  def findNWithPartitionValueDivisibleByMillion: Long = {
    def partitionFunHelper(n: Int, precomputedVals: Map[Int, Long]): Long = {
      val nxtNum = getPartitionsOfNGivenPreviousPartitions(n, precomputedVals)
      if (nxtNum % 1000000 == 0) {
        n
      }
      else {
        partitionFunHelper(n + 1, precomputedVals ++ Map(n -> nxtNum))
      }
    }
    partitionFunHelper(0, Map())
  }
}

 /**
    * Implements Euler's recurrence to compute partitions of a given number.
    *
    * Remove the modulo 10000000 to get the absolute numbers. Change to BigInt to support
    * larger ranges
    *
    * The Map can be removed from the parameters, but that means calculating each of the
    * terms repeatedly.
    *
    * @param n : Number for which partition function P(n) to be calculated
    * @param precomputedVals Map of n -> P(n) as pre computed values. Pass an empty Map first, and
    *                        update the map after every new result.
    * @return
    */
  def getPartitionsOfNGivenPreviousPartitions(n: Int, precomputedVals:Map[Int, Long]): Long = {
    def sumUp(sum:Long, pIdx:Int, sign:Int,n: Int, precomputedVals:Map[Int, Long]): Long = {
      val p1 = (pIdx * (3 * pIdx - 1))/2
      val p2 = ((-1 * pIdx) * ((-3 * pIdx) - 1))/2

      val newSum = sum + ((sign * (if (p1 <= n) precomputedVals(n-p1) else 0)) % 1000000 +
        (sign * (if (p2 <= n) precomputedVals(n-p2) else 0)) % 1000000) % 1000000

      if(p1 >= n && p2 >=n) {
        newSum
      } else {
        sumUp(newSum, pIdx + 1, -1 * sign, n, precomputedVals)
      }
    }
    n match {
      case x if x < 0 => 0
      case x if x == 0 => 1
      case x if x < 4 => x
      case _ => sumUp(0L, 1, 1, n, precomputedVals)
    }
  }

