from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class SuggestionComment(Base):
    __tablename__ = "t_suggestion_comment"

    id = Column(Integer, primary_key=True, nullable=False)
    suggestion_id = Column(Integer, ForeignKey("t_suggestion.id"), nullable=False)
    comment = Column(String(255), nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)

    suggestion = relationship("Suggestion", back_populates="suggestionComment")
