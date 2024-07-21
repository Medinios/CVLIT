import { Response } from "express";
import { responses, responsesKeys } from "../core/utils/responses";
import { CreateCVService, UpdateCVService } from "../services/cvService";

export const CreateCVController = (req: any, res: Response) => {
  try {
    const authInfo = req.authInfo;
    if (!req.CV || !authInfo ) res.status(500).send({ status: responses[responsesKeys.MISSING_FILEDS]});
    CreateCVService({ userId: authInfo.uId, CV: req.CV });
    res.status(200).send({ status: responses[responsesKeys.CREATED_USER_SUCCESS]});
  } catch (error) {
    res.status(500).send({ error: error, status: responses[responsesKeys.CREATED_USER_ERROR]});
  }
};

export const UpdateCVController = (req: any, res: Response) => {
    try {
      const authInfo = req.authInfo;
      const {cvData, cvId} = req;
      if (!req.CV || !authInfo ) res.status(500).send({ status: responses[responsesKeys.MISSING_FILEDS]});
      UpdateCVService({ userId: authInfo.uId ,cvId, cvData });
      res.status(200).send({ status: responses[responsesKeys.CREATED_CV_SUCCESS]});
    } catch (error) {
      res.status(500).send({ error: error, status: responses[responsesKeys.CREATED_CV_ERROR]});
    }
};
