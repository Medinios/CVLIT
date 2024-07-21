import { Router } from "express";
import { createUser } from "../controllers/user";

const userRouter = Router();

userRouter.get("/createUser", createUser);
userRouter.get("/updateCV", updateCV);
userRouter.get("/createCV", updateCV);

export default userRouter;
