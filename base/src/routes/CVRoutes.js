import { Router } from "express";
import { CreateUser } from "../controllers/userController";

const CVRouter = Router();

CVRouter.get("/createUser", CreateUser);

export default userRouter;
