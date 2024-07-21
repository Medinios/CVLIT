export const CreateUser = (req, res) => {
  try {
    const user = getUserData(req);
    if (user) UpsertUser({ newUser: user, upsertIfEmpty: true });
    res.status(200).send({ user });
  } catch (error) {
    res.status(500).send(error);
  }
};
