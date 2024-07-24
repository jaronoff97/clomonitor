import json
import yaml

with open("otel_repos.json", "r") as f:
    json_data = json.load(f)

# YAML template
yaml_template = {
    "name": "open-telemetry",
    "display_name": "OpenTelemetry",
    "description": "High-quality, ubiquitous, and portable telemetry to enable effective observability",
    "category": "observability",
    "logo_url": "https://raw.githubusercontent.com/cncf/artwork/master/projects/opentelemetry/icon/color/opentelemetry-icon-color.svg",
    "devstats_url": "https://opentelemetry.devstats.cncf.io/",
    "accepted_at": "2019-05-07",
    "maturity": "incubating",
    "repositories": []
}

skip_list = [
    "opentelemetry-go-vanityurls",
    "build-tools",
    ".github",
    "opentelemetry-proto-go",
    "wg-prometheus",
    "opentelemetry-go-build-tools",
    "assign-reviewers-action",
    "opentelemetry-network-build-tools",
    "opentelemetry-proto-profile",
    "stackoverflow2slack",
    ".allstar",
    "sig-end-user",
    "sig-contributor-experience",
    "opamp-java",
    "opentelemetry-log-collection",
    "semantic-conventions-java",
    "docs-ja",
    "docs-cn",
    "opentelemetry-profiling",
    "opentelemetry-sqlcommenter",
    "opentelemetry-erlang-api",
    "opentelemetry-js-api"
]

repos = []

# Extracting repository information
for repo in json_data:
    if repo["name"] in skip_list:
        continue
    repo_info = {
        "name": repo["name"],
        "url": repo["html_url"],
        "check_sets": []  # Placeholder for check_sets
    }

    # Determine check_sets based on repository name
    if "instrumentation" in repo["name"] or "contrib" in repo["name"] or "sig" in repo["name"]:
        repo_info["check_sets"].append("code-lite")
    elif "specification" in repo["name"] or "spec" in repo["name"] or "docs" in repo["name"] or "opentelemetry.io" in repo["name"] or "semantic-conventions" in repo["name"]:
        repo_info["check_sets"].append("docs")
    elif "community" in repo["name"]:
        repo_info["check_sets"].append("community")
    elif "collector" in repo["name"]:
        repo_info["check_sets"].append("code")
    else:
        repo_info["check_sets"].append("code")

    repos.append(repo_info)

repos.sort(key=lambda x: x["name"])
yaml_template["repositories"] = repos
# Convert to YAML
yaml_output = yaml.dump([yaml_template], sort_keys=False)

# Print or save the YAML output
# print(yaml_output)

# Optionally, you can save the output to a file
with open("output.yaml", "w") as file:
    file.write(yaml_output)
