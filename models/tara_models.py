class Asset:                                                        #Bauplan namens Asset
    def __init__(self, name, description, interfaces):              #wird aufgerufen, wenn ein neues Objekt der Klasse Asset erstellt wird
        self.name = name                                            #speichere den Namen des Assets in der Instanzvariable self.name
        self.description = description      
        self.interfaces = interfaces

    def __repr__(self):
        return f"Asset: {self.name} | Interfaces: {', '.join(self.interfaces)}"  #gibt eine lesbare Darstellung des Objekts zurück, wenn es ausgegeben wird


asset1 = Asset(
    name = "Keyless Entry System",
    description = "Ermöglicht schlüsselloses Öffnen des Fahrzeugs",
    interfaces = ["Wireless Communication", "ECU", "CAN-Bus"]
)

print(asset1)


class Threat:
    def __init__(self, name, category, description, asset):
        self.name = name
        self.category = category
        self.description = description
        self.asset = asset

    def __repr__(self):
        return f"Threat: {self.name} | Category: {self.category} | Target Asset: {self.asset.name}"

threat1 = Threat(
    name = "Signal Spoofing",
    category = "Spoofing",
    description = "Angreifer sendet gefälschte Signale, um das Keyless Entry System zu manipulieren",
    asset = asset1
)

print(threat1)


class Risk:
    def __init__(self, threat, probability, impact):
        self.threat = threat
        self.probability = probability
        self.impact = impact
        self.risk_level = probability * impact  

    def __repr__(self):
        return f"Risk: {self.threat.name} | Level: {self.risk_level}"
    
risk1 = Risk(
    threat = threat1,
    probability = 4,
    impact = 5
)
    
print(risk1)   