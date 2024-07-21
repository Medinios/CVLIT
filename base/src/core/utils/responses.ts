
export enum responsesKeys {
    CREATED_USER_SUCCESS,
    CREATED_USER_ERROR,
    MISSING_FILEDS,
    CREATED_CV_SUCCESS,
    CREATED_CV_ERROR,
}

export const responses = {
    [responsesKeys.CREATED_USER_SUCCESS]: "User created successfully.",
    [responsesKeys.CREATED_USER_ERROR]: "Failed to create user.",
    [responsesKeys.MISSING_FILEDS]: "Error: Missing Fields.",
    [responsesKeys.CREATED_CV_SUCCESS]: "CV created successfully.",
    [responsesKeys.CREATED_CV_ERROR]: "Failed to create CV.",
}