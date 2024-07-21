import User from "../models/UserModel";

export const CreateUserService = async ({ userId, email }) => {
  try {
    const createdUser = await User.create({
      userId,
      email,
    });
    return createdUser;
  } catch (error) {
    return error;
  }
};

export const updateCVService = async (user) => {
  try {
    const createdUser = await User.create({ userId: user.userId });
    return createdUser;
  } catch (error) {
    return error;
  }
};
