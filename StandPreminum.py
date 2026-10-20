from StandStandard import StandStandard
class StandPremium(StandStandard):

  def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
    super().__init__(codice, superficie, padiglione, prezzo_base)
    self.posizione = posizione

  def calcola_prezzo(self):
    # Sovrapprezzo fisso del 30%
    return self.prezzo_base * 1.30

  def __str__(self):
    stato = (
        f"Assegnato a {self.espositore_assegnato.codice}"
        if self.espositore_assegnato
        else "Disponibile"
    )
    return (
        f"{self.codice}: Premium ({self.posizione}), {self.superficie} mq -"
        f" Padiglione {self.padiglione} - Prezzo:"
        f" {self.calcola_prezzo():.2f}€ - {stato}"
    )