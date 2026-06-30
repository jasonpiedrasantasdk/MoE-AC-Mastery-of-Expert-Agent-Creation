# Example Research Output: LLM VRAM Requirements

**Research ID:** `RES-2024-002`  
**Date:** 2024-03-29  
**Confidence Score:** 0.88  
**Primary Sources:** arXiv papers, llama.cpp documentation, GitHub issues, community benchmarks

---

## Absolute Findings (Tier 1)

### Memory Requirements by Precision

#### Full Precision (FP32/FP16)

- A 70B parameter model at **16-bit precision (FP16)** requires exactly **140 GB** of VRAM for weights alone [arXiv:2304.01234, "Memory Requirements of Large Language Models"]

- Additional memory overhead for:
  - **KV Cache**: ~2-4 GB per concurrent sequence (context-dependent)
  - **Activations**: ~10-20% of weight memory during inference
  - **Optimizer States**: 8-12x weight memory during training (FP32) [arXiv:2101.06043]

#### Quantized Models (INT8/INT4)

- **8-bit quantization (INT8)**: Reduces memory to ~70-75 GB (50% reduction) [llama.cpp documentation, GitHub ggerganov/llama.cpp]

- **4-bit quantization (Q4_K_M/GGUF)**: Reduces memory to ~35-40 GB (75% reduction)
  - Uses mixed precision: some weights at 4-bit, critical layers at higher precision
  - GGUF format includes metadata for layer-specific quantization choices [llama.cpp README]

- **Theoretical Minimum**: At 4-bit, absolute minimum is 35 GB (70B × 4 bits ÷ 8 bits/byte)

### Quantization Accuracy Trade-offs

| Quantization | Memory | Accuracy Retention | Perplexity Delta |
|--------------|--------|-------------------|------------------|
| FP16 | 140 GB | 100% | 0.0 |
| INT8 | 70 GB | 98-99% | +0.05-0.1 |
| Q4_K_M | 38 GB | 95-97% | +0.2-0.4 |
| Q4_0 | 35 GB | 92-95% | +0.4-0.6 |

*Source: arXiv:2308.07022 "Quantization Trade-offs in LLM Inference"*

### Physical Hardware Limitations

- **NVIDIA RTX 4090**: 24 GB GDDR6X VRAM (largest consumer GPU)
- **NVIDIA A100**: 40/80 GB HBM2e VRAM (datacenter GPU)
- **NVIDIA H100**: 80 GB HBM3 VRAM (datacenter GPU)
- **Dual RTX 4090**: 48 GB total (24 GB × 2, but model must fit across both)

**Conclusion**: No single consumer GPU can fit a 70B model at any quantization level entirely in VRAM.

---

## Subjective Context (Tier 2/3)

### High-Signal Observations (Tier 2)

#### llama.cpp GitHub Issues & Discussions

- **CPU Offloading**: Users successfully run 70B models by offloading layers to system RAM
  - Method: `llama.cpp` with `-ngl` flag to specify GPU layers
  - Example: `-ngl 20` offloads 20 layers to GPU, rest to CPU/RAM [GitHub Issue #1234]

- **Performance Characteristics**:
  - **GPU-only (full offload)**: 20-30 tokens/second
  - **Partial offload (DDR5)**: 3-8 tokens/second
  - **CPU-only (DDR5)**: 2-5 tokens/second

- **Memory Bandwidth Bottleneck**:
  - PCIe 4.0 x16: ~32 GB/s theoretical, ~28 GB/s practical
  - DDR5-6000: ~96 GB/s (but higher latency)
  - GPU VRAM: 1000+ GB/s (RTX 4090: 1008 GB/s)
  - **Result**: Offloading incurs 30-50x bandwidth penalty [GitHub Discussion #5678]

#### Benchmarks from Verified Users

| Configuration | Model | Quantization | Tokens/sec | Notes |
|---------------|-------|--------------|------------|-------|
| RTX 4090 (24GB) + DDR5 | 70B | Q4_K_M | 4-6 | 30 layers GPU, rest CPU |
| M2 Ultra (192GB unified) | 70B | Q4_K_M | 8-12 | Full GPU offload possible |
| Dual RTX 3090 (48GB) | 70B | Q4_K_M | 12-15 | Model split across GPUs |
| RTX 4070 (12GB) + DDR4 | 70B | Q4_K_M | 2-3 | Heavy CPU offload |

*Compiled from GitHub Issues, r/LocalLLaMA benchmarks*

### Anecdotal Reports (Tier 3)

#### Reddit r/LocalLLaMA Community Reports

- **RTX 4070 Super Users**: Report "usable but slow" performance with 70B Q4 models
  - Typical setup: 12-16 layers on GPU, rest on CPU
  - Experience: "Acceptable for batch processing, not for real-time chat"
  - System RAM requirement: Minimum 32 GB, recommended 64 GB [Reddit thread, 2024-02]

- **Micro-stutter Reports**: Some users report intermittent stuttering even with sufficient RAM
  - Suspected cause: OS memory pressure, swap usage
  - Mitigation: Close other applications, use dedicated swap partition

#### Personal Blog Benchmarks

- **Undervolting Impact**: Some users report success with GPU undervolting to reduce thermal throttling during long inference sessions [personal blog, 2024-01]

- **Linux vs. Windows**: Consistent reports of 10-20% better performance on Linux due to:
  - Lower OS memory overhead
  - Better CUDA driver efficiency
  - No Windows Defender real-time scanning overhead

---

## Known Implementation Discrepancies

| Aspect | Official/Theoretical | Community Reality | Status |
|--------|---------------------|-------------------|--------|
| **4-bit Minimum VRAM** | "35 GB required" | Users report 12 GB VRAM + 64 GB RAM works | **Context-Dependent** |
| **Token Speed** | "DDR5 bandwidth sufficient" | Real-world speeds 50% lower than theoretical | **Overhead Not Accounted** |
| **Multi-GPU Scaling** | "Linear scaling expected" | 15-20% overhead from PCIe communication | **Documented in Issues** |

---

## Recommendations

### For 12 GB VRAM Systems

```bash
# llama.cpp configuration for 70B model on 12GB VRAM
./main -m models/70B-Q4_K_M.gguf \
       -ngl 12 \              # Load 12 layers to GPU
       -t 8 \                 # Use 8 CPU threads
       -c 4096 \              # Context size
       --memory-f32           # Use FP32 for CPU layers (more stable)

# Expected performance: 2-4 tokens/second
```

### System Requirements for 70B Models

| Component | Minimum | Recommended | Optimal |
|-----------|---------|-------------|---------|
| **VRAM** | 8 GB | 16 GB | 24+ GB |
| **System RAM** | 32 GB | 64 GB | 128 GB |
| **RAM Type** | DDR4 | DDR5-4800 | DDR5-6000+ |
| **Storage** | SATA SSD | NVMe Gen3 | NVMe Gen4 |
| **CPU Cores** | 4 | 8 | 16+ |

### Alternative Approaches

#### Option 1: Smaller Models (Better Experience)

```
Recommended for 12 GB VRAM:
- Llama-2-13B (Q6_K): ~10 GB VRAM, full GPU offload
- Mistral-7B (Q8_0): ~8 GB VRAM, full GPU offload
- Mixtral-8x7B MoE (Q4_K_M): ~26 GB (requires some CPU offload)

Performance: 20-40 tokens/second with full GPU offload
```

#### Option 2: Cloud/Remote Inference

```
Services for 70B models:
- RunPod.io: Rent A100/H100 by hour ($2-4/hour)
- Lambda Labs: Cloud GPU instances
- Together.ai: API access to 70B models
- Anyscale: Hosted LLM inference
```

#### Option 3: Apple Silicon (Unified Memory)

```
M2/M3 Ultra configurations:
- 128 GB unified memory: ~$6000 total system
- 192 GB unified memory: ~$8000 total system
- Performance: 8-15 tokens/second for 70B
- Advantage: Full model in "GPU" memory (unified)
```

---

## Implementation Notes

### llama.cpp Configuration Guide

```bash
# Full configuration for RTX 4070 (12GB) + 64GB DDR5

# Step 1: Download model (Hugging Face)
huggingface-cli download TheBloke/Llama-2-70B-GGUF \
  llama-2-70b.Q4_K_M.gguf \
  --local-dir models

# Step 2: Run with optimal settings
./main -m models/llama-2-70b.Q4_K_M.gguf \
       -ngl 14 \
       -t 10 \
       -c 4096 \
       -b 512 \
       --batch-size 512 \
       -p "User prompt here"

# Parameter explanation:
# -ngl 14: Number of layers to GPU (adjust based on VRAM)
# -t 10: CPU threads (match physical cores)
# -c 4096: Context window size
# -b 512: Batch size for prompt processing
```

### Memory Monitoring

```bash
# Linux: Monitor VRAM and RAM usage
watch -n1 'nvidia-smi && free -h'

# Key metrics:
# - GPU Memory Used: Should be near 12GB limit
# - System RAM Available: Keep >8GB free
# - Swap Usage: Should be zero (indicates RAM pressure)
```

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| OOM on GPU | Too many layers offloaded | Reduce `-ngl` by 2-4 |
| OOM on CPU | Insufficient system RAM | Close applications, add swap |
| Very slow (<1 t/s) | DDR4 bottleneck, wrong thread count | Match `-t` to physical cores |
| Crashes after 30 min | Thermal throttling | Improve cooling, reduce load |

---

## References

### Tier 1 Sources

1. arXiv:2304.01234 "Memory Requirements of Large Language Models" - https://arxiv.org/abs/2304.01234
2. arXiv:2308.07022 "Quantization Trade-offs in LLM Inference" - https://arxiv.org/abs/2308.07022
3. arXiv:2101.06043 "Adafactor: Adaptive Learning Rates" - https://arxiv.org/abs/2101.06043
4. llama.cpp Documentation - https://github.com/ggerganov/llama.cpp
5. GGUF Format Specification - https://github.com/ggerganov/ggml/blob/master/docs/gguf.md

### Tier 2 Sources

6. GitHub Issue: llama.cpp memory optimization - https://github.com/ggerganov/llama.cpp/issues/1234
7. GitHub Discussion: Multi-GPU setup - https://github.com/ggerganov/llama.cpp/discussions/5678
8. Hugging Face: TheBloke model cards - https://huggingface.co/TheBloke

### Tier 3 Sources

9. Reddit r/LocalLLaMA: "70B on 12GB VRAM experience" - https://reddit.com/r/LocalLLaMA/comments/[thread-id]
10. Hacker News: "Running LLMs locally" - https://news.ycombinator.com/item?id=[item-id]
11. Personal Blog: "LLM Inference Benchmarks" - https://[blog-url]/llm-benchmarks

---

## Research Metadata

| Field | Value |
|-------|-------|
| **Research Duration** | 60 minutes |
| **Sources Reviewed** | 31 |
| **Tier 1 Sources** | 5 |
| **Tier 2 Sources** | 3 |
| **Tier 3 Sources** | 23 |
| **Conflicts Identified** | 4 |
| **Conflicts Resolved** | 4 (all documented) |
| **Last Updated** | 2024-03-29 |
| **Confidence Notes** | Hardware benchmarks may vary by specific configuration |
