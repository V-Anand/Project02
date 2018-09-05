package events

import scala.collection.mutable

class EventProcessor {
  private val events = new mutable.HashMap[String, String]()

  def ProcessEvent(event : Event) : Boolean = {
    true
  }

  def GetTotalUniques() : Int = {
    events.size
  }

  def CheckUniques () : List[Event] = {
    List()
  }
}
