package events

import java.util.UUID

trait Event {
  def getSourceAPIKey : String
  def getSourceRemoteIP : String
  def getTenantId : String
  def getActorUuid : UUID
  def getType : String
  def getProperties : String
  def getOccurrenceTime : String
  def getIngestionTime : String
}
