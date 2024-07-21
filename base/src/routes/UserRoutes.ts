import { Router } from "express";
import { CreateUser } from "../controllers/userController";

const userRouter = Router();

userRouter.get("/createUser", CreateUser);

export default userRouter;
