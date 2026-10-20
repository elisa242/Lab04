class StandStandard:
 def __init__(self, codice, superficie, padiglione, prezzo_base):
    self.codice = codice
    self.superficie = superficie
    self.padiglione = padiglione
    self.prezzo_base = prezzo_base
    self.espositore_assegnato = None

def calcola_prezzo(self):
 return self.prezzo_base

def __eq__(self, altro):
    if isinstance(altro, StandStandard):
      return self.codice == altro.codice
    return False

def __lt__(self, altro):
    # Permette di ordinare gli stand in base al prezzo calcolato
    return self.calcola_prezzo() < altro.calcola_prezzo()

def __str__(self):
    stato = (
        f"Assegnato a {self.espositore_assegnato.codice}"
        if self.espositore_assegnato
        else "Disponibile"
    )
    return (
        f"{self.codice}: Standard {self.superficie} mq Padiglione"
        f" {self.padiglione} Prezzo: {self.calcola_prezzo():.2f}€ - {stato}"
    )

def __repr__(self):
    return self.__str__()