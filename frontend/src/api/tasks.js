import {getCSRFToken} from "../utils/csrf";
import apiClient from "./apiClient";

export async function fetchTaskSchema() {
    try {
        const response = await apiClient.get("/tasks/api/schema/task");
        return response.data;
    } catch (error) {
        console.error("Error fetching task schema:", error);
        if (error.response && error.response.data) {
            throw new Error(error.response.data.detail || "Failed to fetch task schema");
        }
        throw new Error("Failed to fetch task schema");
    }
}

export async function createTask(data) {
    try {
        const response = await apiClient.post(
            "/tasks/tasks/",
            data,
            {
                headers: {
                    "X-CSRFToken": getCSRFToken()
                }
            }
        );
        return response.data;
    } catch (error) {
        console.error("Error creating task:", error);
        if (error.response && error.response.data) {
            throw error.response.data;  // Return DRF validation errors
        }
        throw new Error("Failed to create task");
    }
}

export async function updateTaskField(id, patchData) {
    try {
        const response = await apiClient.patch(
            `/tasks/tasks/${id}/`,
            patchData,
            {
                headers: {
                    "X-CSRFToken": getCSRFToken()
                }
            }
        );
        return response.data;
    } catch (error) {
        console.error(`Error updating task ${id}:`, error);
        if (error.response && error.response.data) {
            throw error.response.data;
        }
        throw new Error("Failed to update task");
    }
}

export async function fetchTask(id, include = "") {
    try {
        const params = include ? { include } : {};
        const response = await apiClient.get(`/tasks/tasks/${id}/`, { params });
        return response.data;
    } catch (error) {
        console.error(`Error fetching task ${id}:`, error);
        if (error.response && error.response.data) {
            throw new Error(error.response.data.detail || "Failed to fetch task");
        }
        throw new Error("Failed to fetch task");
    }
}