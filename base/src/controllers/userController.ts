import { Response } from "express";
import { CreateUserService } from "../services/userService";
import { responses, responsesKeys } from "../core/utils/responses";

export const CreateUser = (req: any, res: Response) => {
  try {
    const authInfo = req.authInfo;
    if (authInfo) CreateUserService({ userId: authInfo.uId, email: authInfo.eml });
    res.status(200).send({ status: responses[responsesKeys.CREATED_USER_SUCCESS]});
  } catch (error) {
    res.status(500).send({ error: error, status: responses[responsesKeys.CREATED_USER_ERROR]});
  }
};
