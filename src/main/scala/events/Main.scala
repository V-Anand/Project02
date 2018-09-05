package events
import java.time.LocalDateTime

import scala.util.Random
import java.util.UUID


object Main {
  private val evTypes = Array("ClickEvent", "PageView")
  def genEvent : Event = {
    def getSrcRemoteIP : String = {
      Random.nextInt(256) + "." + Random.nextInt(256) +
        "." + Random.nextInt(256) + "." + Random.nextInt(256)
    }
    new Event {
      override def getSourceAPIKey: String = "U3HN2K8TC" + Random.nextInt(10)

      override def getSourceRemoteIP: String = getSrcRemoteIP

      override def getTenantId: String = "JAB9G" + Random.nextInt(10)

      override def getActorUuid: UUID = UUID.randomUUID()

      override def getType: String = evTypes( Random.nextInt(2) )

      def genRandomReferer(i: Int): String = {
        "https://www.google.com/search?terms=acme+part+" + i
      }

      def genRandomUrl(i: Int): String = {
        "https://www.acme.org/page?part=" + i
      }

      def makeJson: Map[String, String] = {
        val r = Random.nextInt(9)
        Map("URL" -> genRandomUrl(r), "REFERER" -> genRandomReferer(r))
      }

      override def getProperties: Map[String,String] = makeJson

      override def getOccurrenceTime: LocalDateTime = LocalDateTime.now()

      override def getIngestionTime: LocalDateTime = LocalDateTime.now()
    }
  }

  def main(args: Array[String]) : Unit = {
    println("Starting Event Processor Test")
    if (args.length > 0) {
      val count = args(0).toInt
      val genr = new EventProcessor
      for (i <- 0 until count) {
        println(i)
      }
      genr.ProcessEvent( genEvent )
    }
  }
}
