import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
    name: "nokota_mustang.random_int",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "nokota_mustang.random_int") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated ? onNodeCreated.apply(this, []) : undefined;
                this.resultWidget = ComfyWidgets["STRING"](this, "result 🎲", ["STRING", { multiline: false }], app).widget;
            }
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, [message]);
                this.resultWidget.value = message.result[0];
            }
        }
    },
});