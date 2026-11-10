from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, DateTime, CheckConstraint, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from estados import Estado

class Base(DeclarativeBase):
    pass

class Equipo(Base):
    __tablename__ = "equipo"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    stock_disponible: Mapped[int] = mapped_column(Integer, nullable=False)
    prestamos: Mapped[list["Prestamo"]] = relationship(back_populates="equipo")

    __table_args__ = (
        CheckConstraint('stock_disponible >= 0', name='check_stock_disponible'),
    )

    def __repr__(self):
        return f"""
        --- Equipo ---
        ID: {self.id}
        Nombre: {self.nombre}
        Tipo: {self.tipo}
        Stock disponible: {self.stock_disponible}
        """
    
class Estudiante(Base):
    __tablename__ = "estudiante"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    prestamos: Mapped[list["Prestamo"]] = relationship(back_populates="estudiante")

    def __repr__(self):
        return f"""
        --- Estudiante ---
        ID: {self.id}
        Nombre: {self.nombre}
        Correo: {self.correo}
        """


class Prestamo(Base):
    __tablename__ = "prestamo"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    estado: Mapped[Estado] = mapped_column(String(20), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    estudiante_id: Mapped[int] = mapped_column(Integer, ForeignKey("estudiante.id"))
    equipo_id: Mapped[int] = mapped_column(Integer, ForeignKey("equipo.id"))

    estudiante: Mapped["Estudiante"] = relationship(back_populates="prestamos")
    equipo: Mapped["Equipo"] = relationship(back_populates="prestamos")

    __table_args__ = (
        CheckConstraint('cantidad > 0', name='check_cantidad'),
    )

    def __repr__(self):
        return f"""
        --- Prestamo ---
        ID: {self.id}
        Fecha: {self.fecha}
        Estado: {self.estado}
        Cantidad: {self.cantidad}
        ID Estudiante: {self.estudiante_id}
        ID Equipo: {self.equipo_id}
        """
