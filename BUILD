load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")

pybind_extension(
    name = "graph_runner",
    srcs = [
        "cameravtuber_pybind.cc"
    ],
    deps = [
        "@mediapipe//mediapipe/examples/desktop:demo_run_graph_main_gpu",
        "@mediapipe//mediapipe/graphs/hand_tracking:multi_hand_mobile_calculators",
    ],
)
