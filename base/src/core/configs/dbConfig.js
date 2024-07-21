import { Sequelize } from "@sequelize/core";
import { PostgresDialect } from "@sequelize/postgres";

const sequelize = new Sequelize({
  dialect: PostgresDialect,
  database: process.env.DB_DATABASE_NAME,
  user: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  host: process.env.DB_HOST,
  port: 5432,
  ssl: true,
  clientMinMessages: "notice",
});

export default sequelize;
