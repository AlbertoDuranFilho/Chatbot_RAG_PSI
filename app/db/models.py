from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from connection import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(Integer, nullable=False)
    telefone = Column(Integer, nullable=False)
    genero = Column(String)

class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True)
    rua = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    pais = Column(String, nullable=False)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    usuario = relationship("Usuario", back_populates="enderecos")

