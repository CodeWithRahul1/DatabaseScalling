class GeoShardingRouter:
    def db_for_read(self, model, **hints):
        """Route read queries based on region."""
        instance = hints.get("instance")
        if instance and hasattr(instance, "region"):
            return self.get_shard(instance.region)
        return None

    def db_for_write(self, model, **hints):
        """Route write queries based on region."""
        instance = hints.get("instance")
        if instance and hasattr(instance, "region"):
            return self.get_shard(instance.region)
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Allow migrations only on region-based shards."""
        if app_label == 'app':
            return db in ['shard_india', 'shard_usa', 'shard_europe']
        return None

    def get_shard(self, region):
        """Determine which shard to use based on region."""
        if region.lower() == "india":
            return "shard_india"
        elif region.lower() == "usa":
            return "shard_usa"
        elif region.lower() == "europe":
            return "shard_europe"
        return None
