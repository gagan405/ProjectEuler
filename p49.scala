package in.umlaut.euler

object PrimePermutations {

  /**
    * Solves project euler problem 49
    * @param n
    * @param d
    * @return
    */
  def getPrimePermutations(n: Int, d: Int): List[(Int, Int, Int)]= {
    val primes = getPrimesTillN(n).filter(_ > 1000).sorted
    primes.groupBy(int2ListOfDigits(_).sorted.mkString).filter(i => i._2.lengthCompare(d-1) >= 0)
      .map(i =>
        (i._1, uniquePairsOfList(i._2).filter(item => i._2 contains (item._1 + item._2) / 2).map(i => (i._1, (i._1 + i._2) / 2, i._2))))
      .filter(i => i._2.nonEmpty).values.toList.flatten
  }
  
  def int2ListOfDigits(n:Int):List[Int] = Stream.iterate(n)(_ / 10) takeWhile(_ != 0) map(_ % 10) toList
   
   /**
    * Creates pairs of elements from a given list
    * @param series
    * @tparam A
    * @return
    */
  def uniquePairsOfList[A](series: List[A]):List[(A,A)] = {
    for {
      (x, idxX) <- series.zipWithIndex
      (y, idxY) <- series.zipWithIndex
      if idxX < idxY
    } yield (x, y)
  }
}
