import { Request, Response } from "express";

export const CreateUser = (req: any, res: Response) => {
  try {
    const authInfo = req.authInfo;
    console.log(authInfo);
    if (user) UpsertUser({ newUser: user, upsertIfEmpty: true });
    res.status(200).send({ user });
  } catch (error) {
    res.status(500).send(error);
  }
};
