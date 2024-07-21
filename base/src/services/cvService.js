import CV from "../models/CVModel";



export const CreateCVService = async (user) => {
    try {
      const createdCV = await CV.create({ userId: user.userId });
      return createdCV;
    } catch (error) {
      return error;
    }
};

export const UpdateCVService = async ({userId, cvId, cvData}) => {
    try {
      const updatedCV = await CV.find({ where: { id: cvId , userId: userId } })
      .on('success', function (cv) {
        if (cv) {
          cv.update({
            cv: cvData
          })
          .success(function (updatedCV) {
            return updatedCV;
          })
        }
      })
      return updatedCV;
    } catch (error) {
      return error;
    }
};
  