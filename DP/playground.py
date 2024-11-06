@startuml
abstract class Chain{
    - successor: Chain
    + Chain(successor: Chain) <<create>>
    + handle(request)
    - _handle(request)
}

class ConcreteClass1{
    - _handle(request) 
} 
class ConcreteClass2{
    - _handle(request) 
} 

Chain <|-- ConcreteClass1
Chain <|-- ConcreteClass2

@enduml