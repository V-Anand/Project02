package events

import java.time.LocalDateTime
import java.util.UUID

trait Event {
  def getSourceAPIKey : String
  def getSourceRemoteIP : String
  def getTenantId : String
  def getActorUuid : UUID
  def getType : String
  def getProperties : Map[String, String]
  def getOccurrenceTime : LocalDateTime
  def getIngestionTime : LocalDateTime
}
