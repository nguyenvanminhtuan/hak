from sqlalchemy import DateTime, func, Column


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
