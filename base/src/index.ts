import * as dotenv from "dotenv";
dotenv.config();

import cors from "cors";
import express from "express";
import { authMiddleware } from "./core/middlewares/authMiddleware";
import userRouter from "./routes/UserRoutes";

const port = 3002;
const app = express();

app.use(cors());

//routes
app.use("/user", userRouter);

app.get("/", (req, res) => {
  res.send("Not Protected data");
});

app.get("/protected", authMiddleware, (req, res) => {
  res.send({ data: "This is protected data" });
});

app.listen(port, () => {
  console.log(`listening on port ${port}`);
});
