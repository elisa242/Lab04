class Espositore:

  def __init__(self, codice, nome, cognome):
    self.codice = codice
    self.nome = nome
    self.cognome = cognome

  def __eq__(self, altro):
    if isinstance(altro, Espositore):
      return self.codice == altro.codice
    return False

  def __str__(self):
    return f"{self.codice} - {self.nome} {self.cognome}"

  def __repr__(self):
    return f"Espositore('{self.codice}', '{self.nome}', '{self.cognome}')"