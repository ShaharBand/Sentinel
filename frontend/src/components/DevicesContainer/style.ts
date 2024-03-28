import { css } from "@emotion/css";
import { Theme } from "@mui/material";

export const getClasses = (theme: Theme) => ({
    TableContainer: css({
        width: "70vw - 240px", // 20px * 12
        height: "100vh - 240px", // 20px * 12
        padding: "20px",
        boxSizing: "border-box",
        background: theme.palette.primary.main,
        color: theme.palette.text.primary,
        boxShadow: "0px 0px 49px rgba(0, 0, 0, 0.25)",
        borderRadius: "2rem"
  }),
});
