import * as dotenv from "dotenv";
import cors from "cors";
import express from "express";
import { authMiddleware } from "./core/middlewares/authMiddleware";

const app = express();

app.use(cors());

dotenv.config();

const port = 3002;

app.get("/", (req, res) => {
  res.send("Not Protected data");
});

app.get("/protected", authMiddleware, (req, res) => {
  res.send({ data: "This is protected data" });
});

app.listen(port, () => {
  console.log(`listening on port ${port}`);
});
