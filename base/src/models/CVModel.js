import sequelize from "../core/configs/dbConfig";
import User from "./UserModel";

const CV = sequelize.define("Cvs", {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  userID: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: "Users",
    referencesKey: "id",
  },
  CV: {
    type: DataTypes.STRING,
    allowNull: true,
  },
});

CV.hasMany(User, { foreignKey: "userID" });

export default CV;
