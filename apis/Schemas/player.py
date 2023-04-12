from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from apis.Models.player import PlayerModel


class PlayerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PlayerModel
        include_relationships = True
        load_instance = True
