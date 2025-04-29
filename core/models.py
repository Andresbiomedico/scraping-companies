from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CompanyData:
    """Clase para representar los datos de una empresa extraídos de la DIAN."""
    nit: str
    dv: Optional[str] = field(default="")
    razon_social: Optional[str] = field(default="")
    primer_apellido: Optional[str] = field(default="")
    segundo_apellido: Optional[str] = field(default="")
    name: Optional[str] = field(default="")
    otro_nombre: Optional[str] = field(default="")
    fecha_actualizacion: Optional[str] = field(default="")
    estado: Optional[str] = field(default="")
    observacion: Optional[str] = field(default="")

    def to_dict(self):
        """Convierte la instancia a un diccionario."""
        return {
            "nit": self.nit,
            "dv": self.dv,
            "razon_social": self.razon_social,
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "name": self.name,
            "otro_nombre": self.otro_nombre,
            "fecha_actualizacion": self.fecha_actualizacion,
            "estado": self.estado,
            "observacion": self.observacion,
        }