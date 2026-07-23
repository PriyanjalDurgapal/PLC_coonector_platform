<script setup>
import { computed } from "vue"

const props = defineProps({
  object: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits([
  "mousedown",
  "read",
  "write",
])

// ======================
// READ VALUE
// ======================
function buttonClicked() {
  emit("read", props.object)
}

// ======================
// START DRAG
// ======================
function mouseDown(event) {
  emit("mousedown", event)
}

// ======================
// TOGGLE BOOL VALUE
// Double Click:
// 0 -> 1
// 1 -> 0
// ======================
function toggleValue() {

  const newValue =
    Number(props.object.value) === 1 ? 0 : 1

  // Update immediately so the color changes instantly
  props.object.value = newValue

  // Send the SAME object to parent
  emit("write", props.object)
}

// ======================
// BUTTON COLOR
// ======================
const buttonColor = computed(() => {

    console.log(
        "VALUE:",
        props.object.value,
        typeof props.object.value
    )

    return Number(props.object.value) === 1
        ? props.object.on_color
        : props.object.off_color

})         
// ======================
// TOOLTIP
// ======================
const tooltipText = computed(() => {
  return Number(props.object.value) === 1
    ? "Double-click to Stop"
    : "Double-click to Start"
})

// ======================
// STATUS TEXT
// ======================
const statusText = computed(() => {
  return Number(props.object.value) === 1
    ? "ON"
    : "OFF"
})
</script>

<template>
  <div
    class="absolute flex flex-col items-center select-none"
    :style="{
      left: object.x + 'px',
      top: object.y + 'px',
      transform: `rotate(${object.rotation}deg) scale(${object.scale})`,
      transformOrigin: 'center',
    }"
  >
    <button
      class="plc-button"
      :title="tooltipText"
      :style="{
        backgroundColor: buttonColor,
      }"
      @click.stop="buttonClicked"
      @dblclick.stop="toggleValue"
      @mousedown.stop="mouseDown"
    >
      {{ object.label || "BUTTON" }}

      <div class="status">
        {{ statusText }}
      </div>
    </button>

    <div class="hint">
      {{ tooltipText }}
    </div>
  </div>
</template>

<style scoped>

.plc-button{

    width:140px;
    height:60px;

    border:none;
    border-radius:12px;

    color:white;
    font-weight:bold;
    font-size:15px;

    cursor:pointer;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    transition:
        background-color .25s,
        transform .1s,
        box-shadow .15s,
        filter .2s;

    box-shadow:
        0 6px 12px rgba(0,0,0,.25),
        inset 0 2px 2px rgba(255,255,255,.2);

}

.plc-button:hover{

    filter:brightness(1.08);

}

.plc-button:active{

    transform:translateY(3px);

    box-shadow:
        inset 0 4px 8px rgba(0,0,0,.35),
        0 2px 4px rgba(0,0,0,.2);

}

.status{

    margin-top:4px;

    font-size:12px;

    font-weight:600;

    opacity:.9;

}

.hint{

    margin-top:6px;

    font-size:11px;

    color:#475569;

    text-align:center;

}

</style>