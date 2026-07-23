local repository_base = "https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/"
local collection_base = repository_base .. "cadernos-revisao-ecologica/"

function Link(link)
  if link.target:match("^%.%./analyses/") then
    link.target = repository_base .. link.target:gsub("^%.%./", "")
  elseif link.target:match("^caderno%-%d%d%-.*%.md") or link.target:match("^anexo%-%d%d%-.*%.md") then
    link.target = collection_base .. link.target
  end
  return link
end
